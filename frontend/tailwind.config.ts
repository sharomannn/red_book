/* eslint-env node */
import { getIconCollections, iconsPlugin } from '@egoist/tailwindcss-icons'
import type { Config } from 'tailwindcss'

export default {
  content: ['./index.html', './src/**/*.{vue,ts}'],
  theme: {
    colors: {
      'dark-text': '#303045',
      'gray-dark': '#909399',
      'gray': '#B7B7C1',
      'gray-light': '#E1E5EF',
      'white-background': '#F5F7FA',
      'orange-main': '#FD8229',
      'orange-light-hover': '#FFA41B',
      'yellow': '#FFDD00',
      'blue-main': '#1A5CFF',
      'blue-light-hover': '#4F81FF',
      'red': '#E73C47',
      'green': '#26D060',
      'main-dark': '#323544',
      'main-light-gray': '#A8ABB2',
      'background': '#EEF2F6',
      'main-white': '#F0F0F0',
      'main-green': '#67C23A',
    },
    fontFamily: {
      Inter: ['Inter'],
      Manrope: ['Manrope'],
      Roboto: ['Roboto'],
    },
  },
  plugins: [
    // require('@tailwindcss/aspect-ratio'),
    // require('@tailwindcss/typography'),
    // require('@tailwindcss/forms'),
    iconsPlugin({
      collections: getIconCollections(['mdi']),
    }),
  ],
} as Config
