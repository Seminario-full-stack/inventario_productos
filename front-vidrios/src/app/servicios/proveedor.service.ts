import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Proveedor } from '../modelos/proveedor.model';
import { Usuarios } from '../modelos/usuarios.model';
import { promises } from 'dns';

@Injectable({
  providedIn: 'root'
})
export class ProveedorService {

  constructor(private http: HttpClient) { }
listar(): Observable<Proveedor[]> {
return
this.http.get<Proveedor[]>(`${environment.url_gateway}/proveedor`);
}
eliminar(id:string){
return
this.http.delete<Proveedor>(`${environment.url_gateway}/proveedor/${id}`,
);
}
getProveedor(id: string): Observable<Proveedor> {
  return
  this.http.get<Proveedor>(`${environment.url_gateway}/proveedor/${id}`);
  }
  crear(elProveedor: Proveedor) {
  return this.http.post(`${environment.url_gateway}/proveedor`,
  elProveedor);
  }
  editar(id:string,elProveedor:Proveedor) {
  return this.http.put(`${environment.url_gateway}/proveedor/${id}`,
  elProveedor);
  }
}
