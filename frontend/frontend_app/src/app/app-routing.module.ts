import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { PostComponent } from './post/post/post.component';

const routes: Routes = [
  { path: '', component: PostComponent, pathMatch: 'full'},
  // { path: '/', component: PostComponent, pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
