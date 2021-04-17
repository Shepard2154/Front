import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter);

const routes = [
  {
    path: "",
    name: "Home",
    component: () => import("../views/Home.vue"),
  },
  {
    path: "/cabinet",
    name: "Cabinet",
    component: () => import("../views/Cabinet.vue"),
    children: [
      {
        path: "questionary",
        name: "questionary",
        component: () => import("../views/Questionary.vue"),
      },
      {
        path: "statements",
        name: "statements",
        component: () => import("../views/Statements.vue"),
      },
      {
        path: "documents",
        name: "documents",
        component: () => import("../views/Documents.vue"),
      },
      {
        path: "favorites",
        name: "favorites",
        component: () => import("../views/Favorites.vue"),
      },
      {
        path: "ask",
        name: "ask",
        component: () => import("../views/Ask.vue"),
      }
    ]
  },
  {
    path: "/register",
    name: "Registration",
    component: () => import("../views/Registration.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/admin",
    name: "admin",
    component: () => import("../views/Admin.vue"),
    children: [
      {
        path: "login",
        name: "loginAdmin",
        component: () => import("../views/LoginAdmin.vue"),
      },
      {
        path: "profile",
        name: "cabinetAdmin",
        component: () => import("../views/CabinetAdmin.vue"),
        children: [
          {
            path: "contingent",
            name: "contingentAdmin",
            component: () => import("../views/ContingentAdmin.vue"),
          },
          {
            path: "staff",
            name: "staffAdmin",
            component: () => import("../views/StaffAdmin.vue"),
          },
          {
            path: "commission",
            name: "commissionAdmin",
            component: () => import("../views/CommissionAdmin.vue"),
          },
          {
            path: "reports",
            name: "reportsAdmin",
            component: () => import("../views/ReportsAdmin.vue"),
          },
          {
            path: "property",
            name: "propertyAdmin",
            component: () => import("../views/PropertyAdmin.vue"),
          },
        ]
      },
    ]
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  linkActiveClass: "active",
  routes,
});

export default router;
