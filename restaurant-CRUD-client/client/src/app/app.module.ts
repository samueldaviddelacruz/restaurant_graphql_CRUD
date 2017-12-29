import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import {ApolloModule} from 'apollo-angular';
import {HttpLinkModule} from 'apollo-angular-link-http'

import {AppComponent} from './app.component';
import {CategoryService} from './category-service';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ApolloModule,
    HttpLinkModule,
    FormsModule
  ],
  providers: [CategoryService],
  bootstrap: [AppComponent]
})
export class AppModule {
}
