import { Component, Input } from '@angular/core';
import { DatePipe, NgIf } from '@angular/common';

@Component({
  selector: 'app-user-header',
  standalone: true,
  imports: [NgIf, DatePipe],
  templateUrl: './user-header.component.html',
  styleUrls: ['./user-header.component.scss'],
})
export class UserHeaderComponent {
  @Input() user!: { name: string; email: string; phone: string };
  @Input() plan!: { name: string; renewal_date: string };
}
