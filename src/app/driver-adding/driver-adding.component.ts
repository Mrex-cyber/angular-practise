import { Component, Input, Output, EventEmitter } from '@angular/core';
import { IDriver } from '../IDriver';

@Component({
  selector: 'app-driver-adding',
  templateUrl: './driver-adding.component.html',
  styleUrls: ['./driver-adding.component.css']
})
export class DriverAddingComponent {
  @Output() newDriverEvent = new EventEmitter<IDriver>();

  newDriver: IDriver = {id: 1, name: "", age: 18};

  AddNewDriver(id: any, name: string, age: any){
    this.newDriver.id = id;
    this.newDriver.name = name;
    this.newDriver.age = age;
    this.newDriverEvent.emit(this.newDriver);
  }
}
