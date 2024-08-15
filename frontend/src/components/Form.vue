<script setup>
import { ref, watch } from "vue";

const dialog = ref(false);
const valid = ref(false);
const prediction = ref(null);

const formData = ref({
  gender: null,
  race: null,
  parental_level_of_education: null,
  lunch: null,
  test_preparation_couse: null,
  reading_score: null,
  writing_score: null,
});

function validateAndRound(value) {
  let roundedValue = Math.round(value);
  if (roundedValue > 100) {
    roundedValue = 100;
  }

  return roundedValue;
}

async function Predict() {
  prediction.value = null;
  dialog.value = true;
  prediction.value = await PostData("makepredictions");
}

async function PostData(path) {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/" + path, {
      method: "POST",
      body: JSON.stringify(formData.value),
    });
    if (!response.ok) {
      throw new Error(`Response status: ${response.status}`);
    }
    const json = await response.json();
    return json.prediction;
  } catch (error) {
    console.error(error.message);
  }
}

watch(
  () => formData.value.reading_score,
  (newValue, oldValue) => {
    if (newValue !== oldValue) {
      formData.value.reading_score = validateAndRound(newValue);
    }
  }
);

watch(
  () => formData.value.writing_score,
  (newValue, oldValue) => {
    if (newValue !== oldValue) {
      formData.value.writing_score = validateAndRound(newValue);
    }
  }
);
</script>

<template>
  <v-sheet class="mx-auto w-50">
    <v-form fast-fail @submit.prevent v-model="valid">
      <v-select
        label="Gender"
        v-model="formData.gender"
        :items="['female', 'male']"
        :rules="[(v) => !!v || 'Item is required']"
        variant="solo"
      ></v-select>

      <v-select
        label="Race"
        :items="['group A', 'group B', 'group C', 'group D', 'group E']"
        :rules="[(v) => !!v || 'Item is required']"
        variant="solo"
        v-model="formData.race"
      ></v-select>

      <v-select
        label="Parental Level of Education"
        :items="[
          'bachelor\'s degree',
          'some college',
          'master\'s degree',
          'associate\'s degree',
          'high school',
          'some high school',
        ]"
        :rules="[(v) => !!v || 'Item is required']"
        variant="solo"
        v-model="formData.parental_level_of_education"
      ></v-select>

      <v-select
        label="Lunch"
        :items="['standard', 'free/reduced']"
        :rules="[(v) => !!v || 'Item is required']"
        variant="solo"
        v-model="formData.lunch"
      ></v-select>

      <v-select
        label="Test Preparation Course"
        :items="['none', 'completed']"
        :rules="[(v) => !!v || 'Item is required']"
        variant="solo"
        v-model="formData.test_preparation_couse"
      ></v-select>

      <v-text-field
        label="Reading Score"
        variant="solo"
        type="number"
        min="0"
        max="100"
        step="1"
        v-model="formData.reading_score"
        :rules="[(v) => !!v || 'Item is required']"
      ></v-text-field>

      <v-text-field
        label="Writing Score"
        variant="solo"
        type="number"
        min="0"
        max="100"
        step="1"
        v-model="formData.writing_score"
        :rules="[(v) => !!v || 'Item is required']"
      ></v-text-field>

      <v-btn
        :disabled="!valid"
        @click="Predict()"
        class="mt-2 w-25"
        type="submit"
        >Predict</v-btn
      >

      <v-dialog max-width="500" v-model="dialog">
        <v-card title="Predicted Math Score for this student">
          <v-progress-circular
            v-if="prediction == null"
            color="primary"
            indeterminate
            class="ma-auto"
          ></v-progress-circular>
          <v-progress-circular
            v-if="prediction != null"
            class="ma-auto result-circle"
            :size="150"
            :width="12"
            :model-value="prediction"
            color="teal"
          >
            {{ prediction }}
          </v-progress-circular>

          <v-card-actions>
            <v-spacer></v-spacer>

            <v-btn text="Close" @click="dialog = false"></v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-form>
  </v-sheet>
</template>

<style scoped>
.result-circle {
  font-size: 25px;
}
</style>
