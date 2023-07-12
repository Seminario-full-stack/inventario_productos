import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import Swal from 'sweetalert2';
import { Almacenistas } from '../../../modelos/almacenistas.model';
import { AlmacenistasService } from '../../../servicios/almacenistas.service';

@Component({
  selector: 'ngx-crear',
  templateUrl: './crear.component.html',
  styleUrls: ['./crear.component.scss']
})
export class CrearComponent implements OnInit {
  modoCreacion: boolean = true;
  id_almacenista: string = "";
  intentoEnvio: boolean = false;
  elAlmacenista: Almacenistas = {
    cedula: "",
    nombre: "",
    apellido: "",
    celular: "",
    direccion: ""
  }
  
  constructor(private miServicioAlmacenistas: AlmacenistasService,
    private rutaActiva: ActivatedRoute,
    private router: Router) { }

  ngOnInit(): void {
    if (this.rutaActiva.snapshot.params.id_almacenista) {
      this.modoCreacion = false;
      this.id_almacenista = this.rutaActiva.snapshot.params.id_almacenista;
      this.getAlmacenista(this.id_almacenista)
    } else {
  this.modoCreacion = true;
    }
  }

  getAlmacenista(id: string) {
    this.miServicioAlmacenistas.getAlmacenista(id).
      subscribe(data => {
        this.elAlmacenista = data;
      });
  }

  agregar(): void {
    if (this.validarDatosCompletos()) {
      this.intentoEnvio = true;
      this.miServicioAlmacenistas.crear(this.elAlmacenista).
        subscribe(data => {
          Swal.fire(
            'Creado',
            'El Alamcenista ha sido creado correctamente',
            'success'
          )
          this.router.navigate(["pages/almacenistas/listar"]);
        });
    }
  }
  editar(): void {
    this.intentoEnvio = true;
    if (this.validarDatosCompletos()) {
      this.miServicioAlmacenistas.editar(this.elAlmacenista._id, this.elAlmacenista).
        subscribe(data => {
          Swal.fire(
            'Actualizado',
            'El Almacenista ha sido actualizado correctamente',
            'success'
          )
          this.router.navigate(["pages/Almacenistas/listar"]);
        });
    }
  }
  validarDatosCompletos():boolean{
    this.intentoEnvio=true;
    if(this.elAlmacenista.cedula=="" ||
       this.elAlmacenista.nombre=="" ||
       this.elAlmacenista.apellido=="" ||
       this.elAlmacenista.celular=="" ||
       this.elAlmacenista.direccion==""){
      return false;
    }else{
      return true;
    }
  }
}

    



