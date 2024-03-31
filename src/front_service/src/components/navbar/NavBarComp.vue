<template>
  <div class="header">
    <div class="header__inner">
      <div class="header__left">
      </div>
        <div class="header__center">
        <button @click="openMap">Карта</button>
        </div>
        <div class="header__center">
        <button @click="openHome">Календарь</button>
        </div>
    <div>

    </div>
        <div class="header__account">
          <button @click="openExitModal" class="header__account_inner">
            Выйти
          </button>
          <div class="header__account_exit">
            <div @click="exit">
              Выйти
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script lang="ts">
import { ref } from 'vue';
import { useStore } from 'vuex';
import router from '../../router/index'
export default {
  name: 'NavBarComp',
  components:{
    
  },
  data() {
    return {
      navShow: false, 
    };
  },
  setup() {
    const store = useStore();
    const userName = ref('');
    const openExitModal = () => {
      store.commit('common/openModalExit', true)
    };

    const exit = () => {
      store.commit('logout');
      router.push('/signin');
    }
    const openHome = () => {
      router.push('/home');
    }

    const openMap = () => {
      router.push('/map');
    }
    const Logout = () => {
      router.push('/signin');
    }

    // const checkRole = () => {
    //   const getRole = localStorage.getItem('role');
    //   role.value = (getRole === 'true');

    // }

    // onMounted(() =>{
    //   checkRole()
    // })

    return {
      exit,
      openExitModal,
      openHome,
      // openNav,
      openMap,
      userName,
      Logout,
    };
  },
  // computed: {
  //   navShow(): boolean {
  //     return this.$store.state.NAV_SHOW
  //   },
  // }
  // onMounted() {
  //   role.value = localStorage.getItem('role');
  // },
};
</script>

<style >


</style>

