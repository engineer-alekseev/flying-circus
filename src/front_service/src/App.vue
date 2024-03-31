<template>
  <div>
    <NavBarComp
    v-if="$route.name && !['SignIn'].includes($route.name.toString()) && !['SignUp'].includes($route.name.toString())"/>
    <router-view class="content" />
  </div>
</template>

<script lang="ts">
import NavBarComp from '@/components/navbar/NavBarComp.vue'
export default {
  name: 'App',
  components:{
    NavBarComp
  }
}
</script>

<style scoped>
</style>
