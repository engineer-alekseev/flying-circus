<template>
  <div>
    <SelectComp
    label="Выберите этаж"
      :key="selectOptions2"
      :values="selectOptions2"
      :value="currentFloor"
      @change="onFloorChange"
    />
    <SelectComp
      label="Выберите комнату"
      :values="selectOptions"
      :value="currentRoom"
      @change="onRoomChange"
    />
<Calendar />
  </div>
</template>

<script lang="ts">
import { computed, ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import {timeline} from './../../services/index'
import SelectComp from '@/components/fields/SelectComp.vue'
import Calendar from '@/components/pages/Calendar.vue'


export default {
  name: "HomePage",
  components:{
    Calendar, 
    SelectComp,
  },
  data() {
    return{
      meetingId: '', 
      currentFloor: '',
      currentRoom: '',
      bookedTimes: [],
      currentDateTime: null
    }
  },
  setup() {
    const store = useStore();
    const tgId = computed(() => store.state.user.telegram_id);
    const rooms = ref([]);

    const selectOptions = computed(() => {
      return rooms.value.map(room => ({ title: room.name, value: room.id }));
    });

    const selectOptions2 = computed(() => {
      const uniqueLocations = [...new Set(rooms.value.map(room => room.location))];
      return uniqueLocations.map(location => ({ title: location, value: location }));
      });


    onMounted(async () => {
      rooms.value = await timeline.getRooms();
    });

    return {
      tgId,
      rooms,
      selectOptions,
      selectOptions2
    }
  },
  methods: {
    onFloorChange(newValue: string) {
      this.currentFloor = newValue;
    },
    
    formatDateTime(date) {
      let year = date.getFullYear();
      let month = this.pad(date.getMonth() + 1);
      let day = this.pad(date.getDate());
      
      return `${year}-${month}-${day}`;
    },
    pad(number) {
      return number < 10 ? '0' + number : number;
    },

    async onRoomChange(newValue: string) {
      this.currentRoom = newValue;
      const bookedDates = await timeline.getAllBooking();
      if (bookedDates) {
        this.bookedTimes = bookedDates.map(item => ({
          start_time: new Date(item.start_time),
          end_time: new Date(item.end_time)
        }));
        this.$store.commit('setRoom', this.currentRoom);
      }
    }

  },
  mounted() {
    this.currentDateTime = this.formatDateTime(new Date());
  }
}
</script>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>
