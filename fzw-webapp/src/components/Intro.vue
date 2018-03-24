<template>
  <div id="intro">
    <img id="logo" :class="{ land:(page === 0) }" src="static/img/icons/fzw_logo.svg" alt="">
      <div v-if="page === 0" class="">
        <h1>Cześć!</h1>
        <p>Jesteśmy tu po to, aby sprawdzić Twoją odporność na manipulacje w internecie.</p>
      </div>

      <div v-show="page === 1" class="">
        <h3>Jak mamy się do Ciebie zwracać?</h3>
        <div class="input">
          <input v-model="userInfo.name" type="text" name="">
        </div>
      </div>

    <div v-show="page === 2" class="">
      <h3>Na ile oceniasz swoją odporność na manipulacje?</h3>
      <div class="input">
        <select class="input" name="">
          <option v-for="(item, value) in [0,10,20,30,40,50,60,70,80,90,100]" value="">{{item}}%</option>
        </select>
      </div>
    </div>

      <div v-show="page === 3" class="">
        <div id="category-selection">
          <h3>Wybierz obszar, który Cię najbardziej interesuje</h3>
          <div class="input">
            <div class="category-selection">
              <div class="radio">
                <input v-model="userInfo.category" id="rozrywka" type="radio" value="entertainment"></input>
                <label for="rozrywka">
                  <img src="static/img/004-confetti.svg" alt="">Rozrywka
                </label>
              </div>
              <div class="radio">
                <input v-model="userInfo.category" id="sport" type="radio" value="sport">
                <label for="sport">
                  <img src="static/img/001-basketball.svg" alt="">Sport
                </label>
              </div>
              <div class="radio">
                <input v-model="userInfo.category" id="nauka" type="radio" value="science"></input>
                <label for="nauka">
                  <img src="static/img/003-startup.svg" alt="">Nauka
                </label>
              </div>
              <div class="radio">
                <input v-model="userInfo.category" id="polityka" type="radio" value="politics"></input>
                <label for="polityka">
                  <img src="static/img/002-white-house.svg" alt="">Polityka
                </label>
              </div>
            </div>
          </div>
        </div>
      </div>

      <button class="main-cta" @click="incrementPage">dalej</button>
  </div>
</template>

<script>
  export default {
    name: 'intro',
    data () {
      return {
        page: 0,
        userInfo: {
          name: '',
          opinion: 0,
          category: ''
        },
        validationError: false
      }
    },
    computed: {
    },
    methods: {
      incrementPage () {
        ++this.page
      },
      goToGuide () {
        if (this.category !== '') {
          this.$store.commit('setUserInfo', this.userInfo)
          this.$router.push('/guide');
        }
      }
    }

  }
</script>

<style scoped>
  select {
    background: white;
    border: none;
  }
  option{
    font-size: 20%;
  }
  label {
    display: flex;
    justify-content: center;
    align-items: center;
    background: var(--color-blue);
    color: white;
    width: 100%;
    /* height: 90%; */
    border-radius: 2vh;
    transition: .2s;
    font-size: 50%;
    cursor: pointer;
    display: flex;
    flex-direction: column;
  }
  .error{
    background: red;
  }
  .fade-enter-active, .fade-leave-active {
    transition: opacity .5s;
  }
  .fade-enter-active {
    transition-delay: .5s;
  }
  .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
  }

  .category-selection{
    display: flex;
    height: 40vh;
    flex-wrap: wrap;
    justify-content: center;
    font-weight: normal;
    width: 40vh;
  }
  #category-selection input[type="radio"]:checked + label {
    background: var(--color-orange);
    box-shadow: 0 1vh 5vh 0 rgba(239, 66, 12, 0.5);
  }
  .radio {
    width: 44%;
    height: 44%;
    margin: 3%;
  }

  img {
    height: 70%;
  }
  #category-selection input {
    margin: 0;
    display: none;
    color: white;
  }
</style>
