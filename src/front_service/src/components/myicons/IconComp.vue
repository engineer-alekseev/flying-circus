<template>
    <div :class="['ui-icon', { 'ui-icon--bordered': border }]" v-html="iconSvg"/>
</template>

<script lang="ts">
import { computed } from 'vue'
import icons from './icons'

export default {
    name: 'IconComp',
    props: {
        name: String,
        border: {
            type: Boolean,
            default: false
        },
        icons: {
            type: Object as () => typeof icons,
            default: () => icons
        }
    },
    setup(props) {
        const iconSvg = computed(() => {
            const iconName = props.name as keyof typeof icons;
            return icons[iconName] || 'defaultIcon';
        });
        return { iconSvg };
    }

}
</script>

<style lang="scss">
.ui-icon {
    width: 18px;
    height: 18px;
    box-sizing: content-box;
    display: inline-block;

    &--bordered {
        border: 1px solid $color-grey-light;
        border-radius: 6px;
        padding: 10px;
    }

    svg {
        fill: currentColor;
        width: 100%;
        height: 100%;
        display: block;
    }

    svg, rect, mask, circle {
        margin: 0;
        padding: 0;
    }
}
</style>./icons-set./icons
