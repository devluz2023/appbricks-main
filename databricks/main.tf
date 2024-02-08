resource "random_pet" "rg_name" {
  prefix = var.resource_group_name_prefix
}


resource "azurerm_resource_group" "appbricks" {
  location = var.resource_group_location
  name     = random_pet.rg_name.id
}

resource "azurerm_databricks_workspace" "appbricks" {
  name                = "databricks-test"
  resource_group_name = azurerm_resource_group.appbricks.name
  location            = azurerm_resource_group.appbricks.location
  sku                 = "standard"

  tags = {
    Environment = "Production"
  }
}