<template>
  <button @click="$emit('click', $event)" tabindex="-1"
          :disabled="disabled"
          :class="['ui-button',`_${ color }`, `_${ mode }`, { '_disabled': disabled, '_only-icon': (icon && !title) || (!icon && title && typeof title === 'string' && title.length === 1)} ]">

    <slot>
      <IconComp :class="['ui-button-icon', `_${ icon_color}`]" v-if="icon" :name="icon"
              :width="mode === 'mini' ? 16 : 18" :style="{ marginRight: title ? '8px' : '0px' }"/>
      <span v-if="title && typeof title === 'string'">{{ title }}</span>
    </slot>
    <div class="ui-button__loading" v-if="loading">
            <span class="loader">
                <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <g clip-path="url(#clip0_513_19631)">
                        <path d="M10 2.5C14.1422 2.5 17.5 5.85787 17.5 10" stroke="currentColor" stroke-width="2"
                              stroke-linecap="round"/>
                    </g>
                    <defs>
                        <clipPath id="clip0_513_19631">
                            <rect width="20" height="20" fill="currentColor"/>
                        </clipPath>
                    </defs>
                </svg>
            </span>
    </div>
  </button>
</template>

<script lang="ts">
import { PropType } from 'vue'
import IconComp from './../myicons/IconComp.vue'

export default {
  name: 'ButtonComp',
  components: {
    IconComp
  },
  inheritAttrs: false,
  props: {
    title: {
      type: [String, Number]
    },
    loading: {
      type: Boolean,
      default: false
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    color: {
      type: String as PropType<'blue' | 'transparent' | 'white' | 'white-grey' | 'red' | 'red-light' | 'disabled'>,
      default: 'blue',
      validator: val => ['blue', 'transparent', 'white', 'white-grey', 'red', 'red-light', 'disabled'].some(r => r === val)
    },
    icon: {
      type: String,
      default: ''
    },
    icon_color: {
      type: String,
      default: 'initial'
    },
    mode: {
      type: String as PropType<"mini" | "full">,
      default: 'full',
      validator: (value: string) => (['mini', 'full']).indexOf(value) > -1
    },
  }
}
</script>../myicons/IconComp.vue
