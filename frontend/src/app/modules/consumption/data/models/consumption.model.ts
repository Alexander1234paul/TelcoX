export interface DashboardResponse {
  balance: number;
  consumption: {
    data_balance: number;
    voice_balance: number;
    last_update: string;
  };
  last_bill: {
    amount: number;
    status: string;
  };
  plan: {
    name: string;
    renewal_date: string;
  };
  user: {
    name: string;
    email: string;
    phone: string;
  };
}
