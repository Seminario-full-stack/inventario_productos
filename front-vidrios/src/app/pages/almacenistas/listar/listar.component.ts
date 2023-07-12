import { Component, OnInit } from '@angular/core';
import Swal from 'sweetalert2';
import { Almacenistas } from '../../../modelos/almacenistas.model';
import { AlmacenistasService } from '../../../servicios/almacenistas.service';
import { Router } from '@angular/router';

@Component({
  selector: 'ngx-listar',
  templateUrl: './listar.component.html',
  styleUrls: ['./listar.component.scss']
})
export class ListarComponent implements OnInit {
  almacenistas : Almacenistas[];
  nombresColumnas: string[] = ['Cedula','Nombre','Apellido','Celular','Direccion','Opciones'];
  constructor(private miServicioAlmacenistas: AlmacenistasService, private router: Router) { }
  
  ngOnInit(): void {
    this.listar();
  }

  listar():void{
    this.miServicioAlmacenistas.listar().
      subscribe(data => {
      this.almacenistas=data;
    });
  }

  agregar():void{
    console.log("agregando nuevo")
    this.router.navigate(["pages/almacenistas/crear"]);
  }

  editar(id:string):void{
    console.log("editando a "+id)
    this.router.navigate(["pages/almacenistas/actualizar/"+id]);
  }

  eliminar(id:string):void{
    Swal.fire({
      title: 'Eliminar Almacenistas',
      text: "Está seguro que quiere eliminar el Almacenista?",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, eliminar'
    }).then((result) => {
      if (result.isConfirmed) {
        this.miServicioAlmacenistas.eliminar(id).
          subscribe(data => {
            Swal.fire(
              'Eliminado!',
              'El Almacenista ha sido eliminada correctamente',
              'success'
            )
            this.ngOnInit();
          });
      }
    })
  }
}