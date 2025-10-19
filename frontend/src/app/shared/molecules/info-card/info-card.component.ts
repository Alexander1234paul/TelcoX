import { Component, Input } from '@angular/core';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatIconModule } from '@angular/material/icon';
import { NgIf, NgStyle } from '@angular/common'; // ✅ importa NgStyle

@Component({
  selector: 'app-info-card',
  standalone: true,
  imports: [NgIf, NgStyle, MatProgressBarModule, MatIconModule], // ✅ agrégalo aquí
  templateUrl: './info-card.component.html',
  styleUrls: ['./info-card.component.scss'],
})
export class InfoCardComponent {
  @Input() title!: string;
  @Input() value!: string;
  @Input() color = '#004aad';
  @Input() icon = 'info';
  @Input() progress?: number;
}
