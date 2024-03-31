<template>
  <div>
    <form class="form--grid-1" @submit.prevent="handleEmail">
      <InputComp 
        v-bind="validateOptions.email"
        :error="entity_errors.email"
        :modelValue="entity.email"
        @update:modelValue="value => entity.email = value"
      />
      <ButtonComp title="Отправить код на почту" />
    </form>

    <form class="form--grid-1" @submit.prevent="handleSignup">
      <InputComp
        v-bind="validateOptions.secret"
        :error="entity_errors.secret"
        v-model="entitySecret.secret" 
        @update:modelValue="value => entitySecret.secret = value"
      />
      
      <ButtonComp title="Подтвердить" />
    </form>
  </div>
</template>


<script lang="ts">
import InputComp from '@/components/fields/InputComp.vue'
import ButtonComp from '@/components/fields/ButtonComp.vue'
// import { validateModel } from "./../utils/form_utils";
import { auth } from './../services'

export default {
    name: "SignUpPage",
    components: {
      InputComp, ButtonComp
    },
    props: {
      teletgramId: String,
    },
    data() {
      return {
        teletgramId:"",
        secret: "",

        isPerforming: false,

        entity: {
          email: ""
        },
        entitySecret: {
          secret: ""
        },
        entity_errors: {
          email: "",
          secret: ""
        },
        validateOptions: {
          email: {
            label: 'Код из письма',
            validate: {
              required: true
            }
          },
          secret: {
            label: 'Подтвердите код',
          }
          // telegram_id: {
          //   label: '',
          //   type: "string",
          //   validate: {
          //     required: true
          //   }
          // } 
        }
      }
    },
    methods: {
      async handleEmail() {
        const secret = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
        this.$store.commit('setSecret', secret);
        await auth.sendCode(this.entity.email, secret)
      },

      async handleSignup() {
      if (this.entitySecret.secret === this.$store.getters.getSecret){
        const res = await auth.signup(this.entity.email)
          if (res.status === 201){
            this.$router.push("/home");
          }
     
    }

    },
    },
    mounted() {
      this.teletgramId = this.$store.getters.getTgId;
      let {
        setLogin = "",
        setemail = "",
        // fireAuth = false,
      } = this.$route.query

      this.entity.telegram_id = setLogin
      this.entity.email = setemail
    

    // if (fireAuth) {
    //   this.handleLogin()
    // }
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
