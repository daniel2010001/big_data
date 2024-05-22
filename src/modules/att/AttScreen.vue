<template>
  <q-page class="q-ma-md">
    <span class="text-h4"> Extracción de noticias </span>
    <q-separator spaced />
    <div class="rows justify-center">
      <q-form
        @submit="onSubmit"
        @reset="onReset"
        class="q-gutter-md col-xs-6 col-sm-6 col-md-6 q-pt-xl"
      >
        <div class="row justify-center">
          <div class="q-ma-md col-xs-6 col-sm-6 col-md-6 ">
            <br />
            <span class="text-h6 col-xs-6 col-sm-6 col-md-6 q-ma-m"> Extracción de las noticias publicadas en las sigueintes páginas web </span>
            <li class="text-h6"> Los Tiempos </li>
            <li class="text-h6"> El Deber </li>
            <li class="text-h6"> Opinión </li>

            <br /> 
            <div class="row justify-center">
              <q-btn label="extract" type="submit" color="primary"/>
              <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
            </div>

            <br /> <br /> <br />
            <div class="row justify-center">
              <span class="text-h6"> Subir al servidor CentOS? </span>
              <q-btn class="q-ml-xl" label="upload" type="button" color="primary"/>
            </div>
          </div>
          
          <q-date 
            range
            subtitle="Rango de busqueda"
            v-model="dataRange"
            navigationMaxYearMonth="2024"
            navigationMinYearMonth="2017"
          />
        </div>
      </q-form>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref, watch } from 'vue';

export default defineComponent({
  name: 'AttRecolectorDeDatos',
  setup() {
    const serviceType = ref(null);
    const service = ref(null);
    const serviceTypeOptions = ref(['Servicios Móviles', 'Servicios Fijos']);
    const serviceOptions = ref([]);
    const dataRange = ref(null); 

    watch(serviceType, (newValue) => {
      if (newValue === 'Servicios Móviles') {
        serviceOptions.value = [
          {label:'Internet', value: 1},
          {label:'Servicio Movil Prepago', value: 2}
        ];
      } else if (newValue === 'Servicios Fijos') {
        serviceOptions.value = [
          {label:'Internet', value: 3},
          {label:'Servicio Local Telefonia',value: 4}
        ];
      }
    });

    const runPythonScript = async (data) => {
      console.log(data);
      fetch('http://localhost:5000/scraping', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      })
      .then((response) => {
        if (!response.ok) {
          throw new Error('Ocurrió un error al enviar los datos.');
        }
        console.log(response);
      })
      .catch(error => {
        console.error('Error', error);
      })
    };

    return {
      serviceType,
      service,
      serviceTypeOptions,
      serviceOptions,
      dataRange,

      async onSubmit() {
        await runPythonScript({
          parametro1: dataRange.value.from,
          parametro2: dataRange.value.to
        });
      },
      onReset() {
        serviceType.value = null;
        service.value = null;
        serviceTypeOptions.value = ['Servicios Móviles', 'Servicios Fijos'];
        serviceOptions.value = [];
      }
    }
  },
});
</script>
