import 'zone.js'; // 👈 IMPORTANTE: Angular necesita Zone.js
import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { App } from './app/app';

console.log('⚡ Iniciando Angular…');

bootstrapApplication(App, appConfig)
  .then(() => console.log(' App bootstrap completado'))
  .catch((err) => console.error(' Error en bootstrap:', err));
