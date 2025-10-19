import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { DashboardResponse } from '../models/consumption.model';

@Injectable({ providedIn: 'root' })
export class ConsumptionService {
  private baseUrl = 'http://localhost:5000/api/v1/consumption';

  constructor(private http: HttpClient) {}

  getUserConsumption(userId: number): Observable<DashboardResponse> {
    return this.http.get<DashboardResponse>(`${this.baseUrl}/${userId}`);
  }
}
