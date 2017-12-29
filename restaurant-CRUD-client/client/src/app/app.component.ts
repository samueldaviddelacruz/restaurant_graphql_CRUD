import {Component, OnInit} from '@angular/core';
import {CategoryService} from './category-service';
import {DishService} from './dish.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  categories = [];
  isAddingCategory = false;
  newCategoryName = '';
  selectedCategory;
  categoryDishes = [];
  isAddingDish = false;
  newDish = {
    name: '',
    price: 0,
    description: ''
  }

  constructor(private categoryService: CategoryService, private dishService: DishService) {

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

    if (category.isEditing && category.name) {

      const result = await this.categoryService.updateCategory(category);

      const oldObjectIndx = this.categories.findIndex(cat => cat.id === result.id)
      this.categories[oldObjectIndx] = {...result, isEditing: false};

      console.log('update ok');
    }


  }

  async getCategoryDishes(category) {


    const result = await this.dishService.getDishesByCategoryId(category.id);

    const data = result.data.allDishesByCategory.map(
      dish => {
        return {id: dish.id, name: dish.name, description: dish.description, price: dish.price, isEditing: false};
      })
    console.log(data)
    this.categoryDishes = [...data];
    this.selectedCategory = category;
  }

  startAddingDish() {
    this.isAddingDish = true;
  }


  async addDish(dish) {

    if (dish.name.trim()) {
      const result = await this.dishService.createDish(dish, this.selectedCategory.id);

      this.categoryDishes.push(result);
      this.isAddingDish = false;

      this.newDish = {
        name: '',
        price: 0,
        description: ''
      };
    }

  }

  cancelAddDish() {
    this.isAddingDish = false;
  }

  async deleteDish(dish) {

    const deletedCategoryId = await this.dishService.deleteDish(dish.id);

    const index: number = this.categoryDishes.indexOf(dish);

    if (index !== -1) {
      this.categoryDishes.splice(index, 1);
    }

    console.log(this.categoryDishes);
  }

  toggleDishEdit(dish) {
    dish.isEditing = !dish.isEditing;
  }

  async updateDish(dish) {
    if (dish.isEditing && dish.name.trim()) {

      const result = await this.dishService.updateDish(dish);

      const oldObjectIndx = this.categoryDishes.indexOf(dish);

      if (oldObjectIndx !== -1) {
        this.categoryDishes[oldObjectIndx] = {...result, isEditing: false};
      }


      await this.getCategoryDishes(this.selectedCategory);
      console.log('update ok');
    }

  }

  cancelEditDish() {

  }

}


