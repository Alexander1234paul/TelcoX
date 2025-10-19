import { Component, OnInit } from '@angular/core';
import { AsyncPipe, DatePipe, NgClass, NgIf } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { Observable } from 'rxjs';
import { ConsumptionFacade } from '../../domain/consumption.facade';
import { DashboardResponse } from '../../data/models/consumption.model';
import { InfoCardComponent } from '../../../../shared/molecules/info-card/info-card.component';

@Component({
  selector: 'app-consumption-dashboard',
  standalone: true,
  imports: [
    NgClass,
    NgIf,
    AsyncPipe,
    DatePipe,
    MatIconModule,
    MatProgressBarModule,InfoCardComponent
  ],
  templateUrl: './consumption-dashboard.component.html',
  styleUrls: ['./consumption-dashboard.component.scss'],
})
export class ConsumptionDashboardComponent implements OnInit {
  dashboard$!: Observable<DashboardResponse | null>;
  error$!: Observable<string | null>;
  currentTime = new Date();

  constructor(private facade: ConsumptionFacade) {}

  ngOnInit(): void {
    this.dashboard$ = this.facade.dashboard$;
    this.error$ = this.facade.error$;
    this.facade.startPolling(1);

    setInterval(() => (this.currentTime = new Date()), 60000);
  }

  getPercent(value: number, total: number): number {
    return Math.round((value / total) * 100);
  }
}
