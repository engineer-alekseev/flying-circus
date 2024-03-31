<template>
  <label class="ui-field-container" @click="$emit('click', $event)">
      <div class="ui-field-label" v-if="label">
          <span>{{ label }}</span>
      </div>
      <div class="ui-input" :class="[ {'_error': error, '_disabled': disabled, '_icon': text_icon || icon}, `_${ color }` ]">
          <div v-if="icon || text_icon" class="ui-input__icon">
              <IconComp :name="icon" v-if="icon"/>
              <span v-else v-text="text_icon"/>
          </div>
          <input ref="input" :step="step" :name="name" :placeholder="placeholder" v-model="valueSetter" :type="type === 'number' ? 'number' : type" :disabled="disabled || silentDisabled" :readonly="readonly"
              @focus="$emit('focus')" @blur="$emit('blur')" @keydown.enter="$emit('keydown:enter', $event)">
          <div class="ui-input__actions" v-if="actions">
              <button type="button" v-for="action in actions" :key="action.key" @click="$emit(`action:${ action.key }`)">
                  <IconComp :name="action.icon" />
              </button>
          </div>
      </div>
      <button type="button" class="ui-field-under-button" v-if="underButtonText" @click="$emit('underButtonClick')">{{ underButtonText }}</button>
      <div class="ui-field-error" v-show="error">{{ error }}</div>
  </label>
</template>

<script lang="ts">
import { PropType } from 'vue'
import IconComp from './../myicons/IconComp.vue'

export default{
  name: 'InputComp',
  components: {
    IconComp
  },
  inheritAttrs: false,
  props: {
      label: {
          type: String
      },
      step: {
          type: [Number, String],
          default: null
      },
      name: {
          type: String,
          default: ''
      },
      error: {
          type: String
      },
      placeholder: {
          type: String,
          default: undefined
      },
      disabled: {
          type: Boolean,
          default: false
      },
      silentDisabled: {
          type: Boolean,
          default: false
      },
      readonly: {
          type: Boolean,
          default: false,
      },
      color: {
          type: String,
          default: 'grey',
          validator: value => ['white', 'grey'].some(r => r === value)
      },
      modelValue: {
          required: true,
          type: [String, Number] as PropType<string | number>
      },
      icon: {
          type: String,
          default: undefined 
      },
      text_icon: {},
      type: {
          type: String,
          default: 'text'
      },
      locale: {
          type: Boolean,
          default: false
      },
      underButtonText: {
          type: String
      },
      actions: {
          type: Array as PropType<{ icon: string, key: string }[]>,
      }
  },
  computed: {
      valueSetter: {
          get(): string | number {
              if (this.type === 'number' && typeof this.modelValue === 'number') {
                  return this.modelValue
              } else {
                  return this.modelValue
              }
          },
          set(v: string | number): void {
              this.$emit('update:modelValue', v)
          }
      }
  },
}
</script>../myicons/IconComp.vue
