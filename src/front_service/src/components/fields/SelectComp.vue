<template>
    <label class="ui-field-container">
        <div class="ui-field-label" v-if="label">
            <span>{{ label }}</span>
        </div>
        <div class="ui-field-container">
            <div class="ui-field-select-btn">
                <div :class="['ui-field-select-btn__button', { 'ui-field-select-btn__button--opened': opened }]"
                    @click="dropdownOpen">
                    <span v-text="valueTitle"/>

                    <!-- <UiIcon name="arrow_right"/> -->
                </div>
            </div>
            <div class="ui-field-select-dropdown" :class="{_opened: opened}">
                <div class="ui-field-select-dropdown__search">
                    <input v-model="searchInSelect" placeholder="Поиск">
                </div>
                <div >
                    <template v-if="isLoadingErrored">
                        <div class="ui-field-select-dropdown__value _error">
                            Произошла ошибка
                        </div>
                    </template>
                    <template v-else-if="isLoading">
                        <div class="ui-field-select-dropdown__value">
                            Загрузка...
                        </div>
                    </template>
                    <template v-else-if="values.length === 0">
                        <div class="ui-field-select-dropdown__value">
                            {{ placeholder || 'Нет значений' }}
                        </div>
                    </template>
                    <template v-else-if="rowsFilter.length === 0">
                        <div class="ui-field-select-dropdown__value">
                            {{ 'Не найдено' }}
                        </div>
                    </template>
                    <template v-else>
                        <div class="ui-field-select-dropdown__value" v-if="empty_row" @click="selectValue(null)">...</div>
                        <div class="ui-field-select-dropdown__value" v-for="val in rowsFilter" :key="val.value + val.title" :title="val.title"
                            @click="selectValue(val)">
                            {{ val.title }}
                        </div>
                    </template>
                </div>
            </div>
        </div>
        <span class="ui-field-error" v-if="error">{{ error }}</span>
    </label>
</template>

<script>
// import UiIcon from '@/components/icon/UiIcon.vue'

export default {
    name: "SelectComp",
    components: {
        // UiIcon,
    },
    props: {
        values: {
            type: Array,
            default: () => ([])
        },
        isLoading: {
            type: Boolean,
            default: false
        },
        isLoadingErrored: {
            type: Boolean,
            default: false
        },
        placeholder: {
            type: String,
        },
        label: String,
        readonly: Boolean,
        disabled: Boolean,
        error: String,
        value: {
            required: true
        },
        empty_row: {
            type: Boolean,
            default: false
        },
    },
    data() {
        return {
            searchInSelect: '',
            opened: false
        }
    },
    
    computed: {
        valueSetter: {
            get: function () {
                return this.value
            },
            set: function (row) {
                if (typeof row === "object" && row !== null && row.value) {
                    this.$emit('input', (row.value || row.title), row.added)
                    this.$emit('change', (row.value || row.title), row.added)
                } else {
                    this.$emit('input', null)
                    this.$emit('change', null)
                }
                return row
            }
        },

        valueTitle() {
            let q = this.values.find(row => {
                return row.value === this.valueSetter
            })
            if (q) {
                return q.title
            } else {
                return 'Выберите'
            }
        },

        rowsFilter() {
            let s = this.searchInSelect.toLowerCase()
            if (s) {
                return this.values.filter(e => {
                    return e.title ? e.title.toLowerCase().indexOf(s) >= 0 : false
                })
            } else {
                return this.values
            }
        }
    },
    methods: {
        selectValue(value = null) {
            this.opened = false
            this.valueSetter = value
            // this.$emit('change', value);
        },
        dropdownOpen() {
            if (!this.readonly && !this.disabled) {
                this.opened = true
                this.$emit('open')
            }
        },
        clickHandler(e) {
            if (!this.$el.contains(e.target)) {
                this.opened = false
            }
        }
    },
    mounted() {
        window.addEventListener('click', this.clickHandler)
    },
    beforeDestroy() {
        window.removeEventListener('click', this.clickHandler)
    }
}
</script>
