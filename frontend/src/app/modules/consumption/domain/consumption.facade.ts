import { Injectable } from '@angular/core';
import { BehaviorSubject, catchError, interval, of, switchMap } from 'rxjs';
import { ConsumptionService } from '../data/services/consumption.service';
import { DashboardResponse } from '../data/models/consumption.model';

@Injectable({ providedIn: 'root' })
export class ConsumptionFacade {
  private dashboardSubject = new BehaviorSubject<DashboardResponse | null>(null);
  private errorSubject = new BehaviorSubject<string | null>(null);

  dashboard$ = this.dashboardSubject.asObservable();
  error$ = this.errorSubject.asObservable();

  constructor(private service: ConsumptionService) {}

  startPolling(userId: number): void {
    interval(5000)
      .pipe(
        switchMap(() =>
          this.service.getUserConsumption(userId).pipe(
            catchError(() => {
              this.errorSubject.next('Error al actualizar datos');
              return of(null);
            })
          )
        )
      )
      .subscribe((data) => {
        if (data) this.dashboardSubject.next(data);
      });
  }
}
