<template>
    <div>
    <span v-if="!isLoaded">Loading...</span>
      <telegram-login-temp
          mode="callback"
          telegram-login="siteauth_bot"
          @loaded='telegramLoadedCallbackFunc'
          @callback="yourCallbackFunction"
          size="large"
      />
    </div>
</template>

<script lang="ts">
import { onMounted } from 'vue'
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useStore } from 'vuex';
import { telegramLoginTemp } from 'vue3-telegram-login'
import { auth } from '../../../services'
export default {
  name: "AuthTelegramComp",
  components:{
    telegramLoginTemp
  },
  setup(){
    const router = useRouter()
    const isLoaded = ref(false)
    const store = useStore();

    // const checkAuth = async () => {
    //   const telegram_id = store.getters.getTgId;
    //   const email = store.getters.getEmail;
    //   if (telegram_id && email){
    //     router.push('/home')
    //   }
    // }

    async function telegramLoadedCallbackFunc () {
      isLoaded.value = true
    }

    async function yourCallbackFunction(user: any) {
      store.commit('setTgId', user.id)
      // alert(user.id)
      const userInfo = await auth.user_auth(user.id)
        if (userInfo) {
          store.commit('user/setUser', userInfo)
          router.push('/home')
        } else {
          router.push('/signup')
        }
    }

    onMounted(async() => {
      // await checkAuth()
    })

    return({
      isLoaded,
      telegramLoadedCallbackFunc,
      yourCallbackFunction

    })
  }
}
</script>