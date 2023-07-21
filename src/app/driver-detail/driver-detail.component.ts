import { Component, Input, Output, EventEmitter } from '@angular/core';
import { IDriver } from '../IDriver';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';
import { DriverService } from '../driver.service';


@Component({
  selector: 'app-driver-detail',
  templateUrl: './driver-detail.component.html',
  styleUrls: ['./driver-detail.component.css']
})
export class DriverDetailComponent {
  @Input() driver: IDriver | undefined;

  constructor (
    private route: ActivatedRoute,
    private driverService: DriverService,
    private location: Location
  ) { }

  ngOnInit(): void {
    this.getDriver();
  }

  getDriver(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));

    this.driverService.getDriver(id).subscribe(driver => this.driver = driver);
  }

  goBack(): void {
    this.location.back();
  }
}
