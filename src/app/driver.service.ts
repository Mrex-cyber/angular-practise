import { Injectable } from '@angular/core';
import { IDriver } from './IDriver';
import { DRIVERS } from './moch-drivers';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';

import { HttpClient, HttpHeaders } from '@angular/common/http';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpRequest } from '@angular/common/http';

@Injectable({ providedIn: 'root' })

export class DriverService {
  //private driversUrl = 'https://localhost:4201//api/drivers';
  private driversUrl = 'http://localhost:5185/api/drivers';

  httpOptions = {
     headers: new HttpHeaders({ 'Content-Type' : 'application/json' })
     };

  constructor(private http: HttpClient, private messageService: MessageService) { }
  drivers : IDriver[] = [];

  getDrivers(): Observable<IDriver[]> {
    return this.http.get<IDriver[]>(this.driversUrl)
    .pipe(
      tap(_ => this.log('fetched drivers')),
      catchError(this.handleError<IDriver[]>('getDrivers', []))
      );
  }

  private handleError<T>(operation = 'operation', result?: T){
    return (error: any): Observable<T> => {
      console.error(error);

      this.log(`${operation} failed: ${error.message}`);

      return of(result as T);
    }
  }

  getDriver(id: number): Observable<IDriver> {
    const driver = DRIVERS.find(dr => dr.id === id)!;

    this.messageService.add(`DriverService: fetched driver id=${id}`);
    return of(driver);
  }

  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }

}
