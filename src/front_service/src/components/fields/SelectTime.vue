<template>
    <div>
        <VueDatePicker 
            class="select-time"
            v-model="date" 
            time-picker
        >
        </VueDatePicker>
    </div>
</template>

<script lang="ts">
import VueDatePicker from '@vuepic/vue-datepicker';
import '@vuepic/vue-datepicker/dist/main.css'

export default {
    name: "SelectTime",
    components: {
        VueDatePicker
    },
    // props: {
    //     showTime: Boolean
    // },
    data() {
        return {
            date: new Date(),
        }
    },
    methods: {
        abc() {
            // alert(this.date)
        }
    }
}
</script>

<style scoped>
.select-time{
    position: absolute;
}
</style>

  
  
  