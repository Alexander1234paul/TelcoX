import { Routes } from '@angular/router';
import { ConsumptionDashboardComponent } from './modules/consumption/presentation/consumption-dashboard/consumption-dashboard.component';

export const routes: Routes = [
  { path: '', component: ConsumptionDashboardComponent },
  { path: '**', redirectTo: '', pathMatch: 'full' },
];
