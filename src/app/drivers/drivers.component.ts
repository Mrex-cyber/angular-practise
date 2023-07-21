import { Component, OnInit } from '@angular/core';
import { IDriver } from '../IDriver';
import { DriverService } from '../driver.service';
import { MessageService } from '../message.service';


@Component({
  selector: 'app-drivers',
  templateUrl: './drivers.component.html',
  styleUrls: ['./drivers.component.css'],
  inputs: ['name', 'age']
})
export class DriversComponent {
  drivers: IDriver[] = [];

  AddDriver(driver: IDriver){
    this.drivers.push(driver);
  }

  getDrivers(): void {
    this.driverService.getDrivers().subscribe(drivers => this.drivers = drivers);
  }
  constructor(private driverService: DriverService, private messageService: MessageService) { }

  ngOnInit():void {
    this.getDrivers();
  }


}
