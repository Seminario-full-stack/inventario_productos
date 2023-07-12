import { Component, NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { patch } from '@nebular/theme';
import { ListarComponent } from './listar/listar.component';
import { CrearComponent } from './crear/crear.component';

const routes: Routes = [
  {
    path:'listar',
    component:ListarComponent
  },
  {
    path:'crear',
    component:CrearComponent
  },
  {
    path:'actualizar/:id_proveedor',
    component: CrearComponent
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProveedorRoutingModule { }
