import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ListarComponent } from './listar/listar.component';
import { CrearComponent } from './crear/crear.component';

const routes: Routes = [
{
  path:'listar',
  component: ListarComponent
  },
{
  path:'crear',
  component: CrearComponent
  },
  {
    path:'actualizar/:id_estudiante',
    component: CrearComponent
    }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductoRoutingModule { }
