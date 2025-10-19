import {
  HttpErrorResponse,
  HttpInterceptorFn,
} from '@angular/common/http';
import { inject } from '@angular/core';
import { catchError, throwError } from 'rxjs';
import { NotificationService } from '../services/notification.service';

export const errorInterceptor: HttpInterceptorFn = (req, next) => {
  const notifier = inject(NotificationService);

  return next(req).pipe(
    catchError((error: HttpErrorResponse) => {
      let message = 'Ocurrió un error inesperado';

      if (error.status === 0) {
        message = 'No se pudo conectar con el servidor';
      } else if (error.status === 404) {
        message = 'El recurso solicitado no existe';
      } else if (error.status === 500) {
        message = 'Error interno del servidor';
      } else if (error.error?.message) {
        message = error.error.message;
      }

      notifier.showError(message);
      return throwError(() => error);
    })
  );
};
