import { NgModule } from '@angular/core';
import { RouterModule, Routes} from '@angular/router';
import { DriversComponent } from './drivers/drivers.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { DriverDetailComponent } from './driver-detail/driver-detail.component';

const routes: Routes = [
  { path: "", redirectTo: "/dashboard", pathMatch: "full" },
  { path: "dashboard", component: DashboardComponent },
  { path: 'detail/:id', component: DriverDetailComponent },
  { path: "drivers", component: DriversComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
