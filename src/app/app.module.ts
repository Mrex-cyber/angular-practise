import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { DriversComponent } from './drivers/drivers.component';

import { FormsModule } from '@angular/forms';
import { DriverDetailComponent } from './driver-detail/driver-detail.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './app-routing.module';
import { DashboardComponent } from './dashboard/dashboard.component';

import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from "@angular/common/http";

@NgModule({
  declarations: [
    AppComponent,
    DriversComponent,
    DriverDetailComponent,
    MessagesComponent,
    DashboardComponent,
  ],
  imports: [
    FormsModule,
    AppRoutingModule,
    BrowserModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
