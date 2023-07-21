import { Component, OnInit } from '@angular/core';
import { IDriver } from '../IDriver';
import { DriverService } from '../driver.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {

  drivers: IDriver[]= [];

  constructor(private driverService: DriverService){ }

  ngOnInit(): void {
    this.getDrivers();
  }

  getDrivers(): void {
    this.driverService.getDrivers().subscribe(drivers => this.drivers = drivers.slice(1, 5));
  }
}
