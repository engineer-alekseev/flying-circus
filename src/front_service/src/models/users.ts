export interface User {
    role: string,
    telegram_id: string,
    id: string,
    auth_method: string,
    email: string,
  }
  
  export interface UserGet extends User {
    id: string
  }
  
  export interface UserRole {
    role: string
  }
