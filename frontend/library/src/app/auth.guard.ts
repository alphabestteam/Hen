import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';


export const authGuard: CanActivateFn = (route, state) => {
  
  const session = sessionStorage.getItem('id');
  console.log(session);
  
  const router = inject(Router)

  
  if (!session)  {
    router.navigate(['login'])
    return false
  } else {
    return true
  }
 };