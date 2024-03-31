<template>
  
    <vue-cal
      
      :events="events"
      @cell-click="addEvent"
    >
    </vue-cal>

</template>

<script>
import { ref } from "vue"
import VueCal from 'vue-cal';
import 'vue-cal/dist/vuecal.css';

export default {
  name: 'Calendar',
  components: {
    VueCal
  },

  data() {
    return {
      events: [],
    };
  },
  methods: {
  addEvent(event) {
    this.events.push({
      start: event,
      end: new Date(event.getTime() + 60 * 60 * 1000),
      title: 'Новое событие',
      class: 'custom-event',
    });
  },
},

};

</script>
