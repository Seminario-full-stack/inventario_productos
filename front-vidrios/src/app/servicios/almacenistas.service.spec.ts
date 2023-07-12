import { TestBed } from '@angular/core/testing';

import { AlmacenistasService } from './almacenistas.service';

describe('AlmacenistasService', () => {
  let service: AlmacenistasService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AlmacenistasService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
