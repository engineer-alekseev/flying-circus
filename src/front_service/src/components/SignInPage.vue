<template>
  <div>
    <AuthTelegramComp />
    <ButtonComp :loading="isPerforming" title="Войти Через Git"/>
  </div>
</template>

<script lang="ts">
import ButtonComp from '@/components/fields/ButtonComp.vue'
import AuthTelegramComp from '@/components/fields/auth/AuthTelegramComp.vue'
// import { iModelEntity, iModelEntityErrors, iModelOptions } from "./../models/form_data";

export default {
    name: "SignInPage",
    header: "Авторизация",
    components: {
      ButtonComp, AuthTelegramComp
    },
    data() {
      return {
        isPerforming: false,
      //   entity: {
      //     username: "",
      //     password: ""
      //   } as iModelEntity,
      //   entity_errors: {
      //     username: "",
      //     password: ""
      //   } as iModelEntityErrors,
      //   validateOptions: {
      //     username: {
      //       label: 'id',
      //       validate: {
      //         required: true
      //       }
      //     },
      //     password: {
      //       label: 'id',
      //       type: "password",
      //       validate: {
      //         required: true
      //       }
      //     }
      //   } as iModelOptions
      }
    },
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>



