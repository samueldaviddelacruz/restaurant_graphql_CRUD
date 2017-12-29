import {Component, OnInit} from '@angular/core';
import {CategoryService} from './category-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  categories = [];
  isAddingCategory = false
  newCategoryName = '';

  constructor(private categoryService: CategoryService) {

  }

  async ngOnInit() {

    const result = await this.categoryService.getAllCategories();
    this.categories = [...result];

  }

  startAddingCategory() {
    this.isAddingCategory = true;
  }

  async addCategory(name) {
    if (name.trim()) {
      const result = await this.categoryService.createCategory(name);

      this.categories.push(result);
      this.isAddingCategory = false;

      this.newCategoryName = '';
    }
  }

  cancelAddCategory() {
    this.isAddingCategory = false;
  }


  toggleEdit(category) {

    category.isEditing = !category.isEditing;

  }

  async deleteCategory(category) {
    const deletedCategoryId = await this.categoryService.deleteCategory(category.id);

    const index: number = this.categories.indexOf(category);

    if (index !== -1) {
      this.categories.splice(index, 1);
    }

    console.log(this.categories);
  }

  async updateCategory(category) {

    if (category.isEditing) {

      const result = await this.categoryService.updateCategory(category);

      const oldObjectIndx = this.categories.findIndex(cat => cat.id === result.id)
      this.categories[oldObjectIndx] = {...result, isEditing: false};

      console.log('update ok');
    }


  }

}


