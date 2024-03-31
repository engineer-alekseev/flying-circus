import { createStore } from 'vuex';
import { User } from './../models/users';
import createPersistedState from 'vuex-persistedstate'

interface RootState {
  user: User,
  secret: string,
  roomId: string
}

export default createStore({
  plugins: [createPersistedState()],
  state(): RootState {
    return {
      user: {
        role: "",
        telegram_id: "",
        id: "",
        auth_method: "",
        email: "",
      },
      secret: "",
      roomId: ""
    };
    
  },
  mutations: {
    setUser(state: RootState, updatedUser: User) {
      state.user = { ...state.user, ...updatedUser };
    },
    setTgId(state: RootState, telegram_id: string) {
      state.user.telegram_id = telegram_id;
    },
    setSecret(state: RootState, secret: string) {
      state.secret = secret;
    },
    setRoom(state: RootState, roomId: string) {
      state.roomId = roomId;
    },
    logout(state: RootState) {
      state.user = {
        role: "",
        telegram_id: "",
        id: "",
        auth_method: "",
        email: "",
      };
    },
    // setCurrentTask(state: RootState, current_task: TaskState) {
    //   state.user.current_task = current_task;
    // },
  },
  getters: {
    getUser(state: RootState): User {
      return state.user;
    },
    getTgId(state: RootState): string {
      return state.user.telegram_id;
    },
    getSecret(state: RootState): string {
      return state.secret;
    },
    getEmail(state: RootState): string {
      return state.user.telegram_id;
    },
    getRoom(state: RootState): string {
      return state.roomId;
    },
    // getCurrentTask(state: RootState): TaskState {
    //   return state.user.current_task;
    // },
  },
  
});
