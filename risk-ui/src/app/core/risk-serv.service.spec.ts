import { TestBed } from '@angular/core/testing';

import { RiskServService } from './risk-serv.service';

describe('RiskServService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: RiskServService = TestBed.get(RiskServService);
    expect(service).toBeTruthy();
  });
});
