<template>
  <div id="quest">
    <svg class="defs-only">
      <filter id="colorize-card" color-interpolation-filters="sRGB"
              x="0" y="0" height="100%" width="100%">
        <feColorMatrix type="matrix"
          values="1.0 0.0 0.0 0.0  0
                  0.0 1.0 0.0 0.0  0
                  0.0 0.0 1.0 0.0  0
                  0.0 0.0 0.0 1.0  0" />
      </filter>
    </svg>
    <div class="container" v-for="(q, index) in questions" :key="q.newsId">
      <transition
        name="question-transition"
        v-on:leave="leaveQuestion"
      >
        <div class="question" v-if="index === questionIndex">
          <pie-chart id="counter" :numerator="countdownSeconds" :denominator="questionTimeoutSeconds" :textPercent="false"/>
          <div class="card">
            <img :src="q.imageUrl"/>
          </div>
          <div class="buttons">
            <button class="secondary-cta answer" v-on:click="answer('yes')">klikam</button>
            <button class="secondary-cta answer" v-on:click="answer('no')">nie klikam</button>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import Velocity from 'velocity-animate';
import { mapMutations } from 'vuex';
import { QUESTION_TIMEOUT } from '../consts';
import PieChart from '@/components/PieChart'

export default {
  name: 'quest',
  components: {
    PieChart
  },
  beforeRouteEnter (to, from, next) {
    next((vm) => {
      vm.generateQuiz();
      vm.startQuestionTimeout();
      vm.startTicker();
    });
  },
  beforeRouteLeave (to, from, next) {
    this.stopQuestionTimeout();
    this.stopTicker();
    next();
  },
  data: () => ({
    tick: Date.now(),
  }),
  computed: {
    question () {
      return this.$store.getters.currentQuizQuestion;
    },
    questions () {
      return this.$store.getters.quizQuestions;
    },
    questionIndex () {
      return this.$store.getters.quizQuestionIndex;
    },
    questionNumber () {
      return this.$store.getters.quizQuestionIndex + 1;
    },
    countdownSeconds () {
      const delta = this.tick - this.questionStartTime;
      return Math.ceil((QUESTION_TIMEOUT - delta) / 1000);
    },
    questionTimeoutSeconds () {
      return QUESTION_TIMEOUT / 1000
    }
  },
  methods: {
    ...mapMutations([
      'answerQuizQuestion',
      'omitQuizQuestion',
      'generateQuiz',
    ]),
    leaveQuestion (el, done) {
      // we already switched to new question, so get the previous one
      const q = this.questions[this.questionIndex - 1];
      const cardEl = el.querySelector('.card');
      const translateVal = document.body.clientWidth;
      const translateX = q.expectedAnswer === 'yes' ? -translateVal : translateVal;
      // const filterId = q.answer === q.expectedAnswer ? 'colorize-green' : 'colorize-red'
      const colorChannel = q.answer === q.expectedAnswer ? 1 : 0;
      const filterEl = document.getElementById('colorize-card');
      const matrixEl = filterEl.querySelector('feColorMatrix');
      matrixEl.setAttribute('values', this.colorizeMatrixString(colorChannel, 0));
      cardEl.style.filter = 'url(#colorize-card)';
      Velocity(cardEl, {
        translateX,
      }, {
        duration: 1000,
        progress: (elements, complete) => {
          matrixEl.setAttribute('values', this.colorizeMatrixString(colorChannel, complete));
        },
      });
    },
    colorizeMatrixString (channel, t) {
      const A = [
        [1 - t, 0, 0, 0],
        [0, 1 - t, 0, 0],
        [0, 0, 1 - t, 0],
        [0, 0, 0, 1],
      ];
      for (let j = 0; j < 3; ++j) {
        A[channel][j] += t / 3;
      }
      const values = [];
      for (let i = 0; i < 4; ++i) {
        for (let j = 0; j < 4; ++j) {
          values.push(A[i][j]);
        }
        values.push(0);
      }
      return values.join(' ');
    },
    answer (a) {
      this.answerQuestionOrEndQuiz(a);
    },
    answerQuestionOrEndQuiz (answer) {
      this.stopQuestionTimeout()
      this.answerQuizQuestion({ answer });
      if (this.$store.getters.isQuizFinished) {
        this.goToResults();
      } else {
        this.startQuestionTimeout();
      }
    },
    omitQuestionOrEndQuiz () {
      this.omitQuizQuestion();
      if (this.$store.getters.isQuizFinished) {
        this.goToResults();
      } else {
        this.startQuestionTimeout();
      }
    },
    goToResults () {
      this.$router.push('/results');
    },
    stopQuestionTimeout () {
      clearTimeout(this.questionTimeout)
    },
    startQuestionTimeout () {
      clearTimeout(this.questionTimeout)
      this.questionStartTime = Date.now();
      this.questionTimeout = setTimeout(() => {
        this.omitQuestionOrEndQuiz();
      }, QUESTION_TIMEOUT);
    },
    startTicker () {
      this.tickInterval = setInterval(() => {
        this.tick = Date.now();
      }, 100);
    },
    stopTicker () {
      clearInterval(this.tickInterval);
    },
  }
}
</script>

<style scoped>
  .container{
    position: absolute;
    width: 80%;
    /* top: 0; */
  }
  .question {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
  }
  #counter{
    width: 18vh;
  }
  img{
    width: 100%;
  }
  button.answer{
    padding: 2vh 1vh;
    width: 45%;
  }

  .buttons {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    width: 100%;
  }

  .defs-only {
    height: 0;
    width: 0;
  }

  .question-transition-enter {
    transform: translateY(100vmax);
  }

  .question-transition-enter-active {
    transition: all 2s ease;
  }

  .question-transition-leave-active {
    transition: all 1s ease;
  }

  .question-transition-leave-to {
    opacity: 0;
  }

</style>
