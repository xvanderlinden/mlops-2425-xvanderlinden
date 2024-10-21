import globals from 'globals';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import js from '@eslint/js';
import { FlatCompat } from '@eslint/eslintrc';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const compat = new FlatCompat({
  baseDirectory: __dirname,
  recommendedConfig: js.configs.recommended,
  allConfig: js.configs.all,
});

export default [...compat.extends('eslint:recommended'), {
  languageOptions: {
    globals: {
      ...globals.node,
      ...globals.mocha,
    },

    ecmaVersion: 12,
    sourceType: 'module',
  },

  rules: {
    indent: ['error', 2, {
      SwitchCase: 1,
    }],

    'linebreak-style': ['error', 'unix'],
    quotes: ['error', 'single'],
    semi: ['error', 'always'],
    'comma-dangle': ['error', 'always-multiline'],
    'no-tabs': ['error'],

    'max-len': ['error', {
      code: 120,
      tabWidth: 2,
    }],

    'arrow-parens': ['error', 'always'],

    'brace-style': ['error', '1tbs', {
      allowSingleLine: false,
    }],

    'no-inner-declarations': 'off',
  },
}];