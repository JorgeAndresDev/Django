document.addEventListener("DOMContentLoaded", async function () {
    const ProductTableBody = document.getElementById("ProductTableBody");
    const ProductTable = document.getElementById("ProductTable");
    const ProductLoading = document.getElementById("ProductLoading");

    // Función para obtener los productos desde la API
    async function getProducts() {
        try {
            const response = await fetch("http://127.0.0.1:9000/products"); // URL corregida
            if (!response.ok) {
                throw new Error(`Error ${response.status}: ${response.statusText}`);
            }
            const data = await response.json();
            return data;
        } catch (error) {
            console.error("Error:", error);
            return null;
        }
    }

    // Obtener los productos
    const products = await getProducts();

    if (products && products.length > 0) {
        ProductLoading.classList.add("d-none");
        ProductTable.classList.remove("d-none");

        ProductTableBody.innerHTML = "";
        let counter = 1;
        products.forEach(product => {
            ProductTableBody.innerHTML += `
                <tr class="align-items-center product-row">
                    <td>${counter}</td>
                    <td>${product.nombre}</td>
                    <td>${product.precio}</td>
                    <td>${product.cantidad}</td>
                    <td>
                        <div class="d-flex flex-row gap-2">
                            <div data-bs-toggle="tooltip" data-bs-custom-class="tooltip-inverse" data-bs-placement="top" title="Editar">
                                <a class="btn btn-sm btn-icon btn-flex btn-light-primary fw-bold" data-bs-toggle="modal" data-bs-target="#modal_update_${product.id}">
                                    <i class="ki-duotone ki-notepad-edit fs-3">
                                        <span class="path1"></span>
                                        <span class="path2"></span>
                                    </i>
                                </a>
                            </div>

                            <a class="btn btn-sm btn-flex btn-icon btn-light-danger fw-bold" data-bs-toggle="tooltip"  
                            data-bs-custom-class="tooltip-inverse" data-bs-placement="top" title="Eliminar" onclick="removeProduct('${product.id}', '${product.nombre}')">
                                <i class="ki-duotone ki-trash fs-3">
                                    <span class="path1"></span>
                                    <span class="path2"></span>
                                    <span class="path3"></span>
                                    <span class="path4"></span>
                                    <span class="path5"></span>
                                </i>
                            </a>
                        </div>
                    </td>
                </tr>
            `;
            counter += 1;
        });

        // Inicializar tooltips
        const response = await fetch("http://127.0.0.1:9000/products");
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });

    } else {
        ProductLoading.classList.add("d-none");
        ProductTableBody.innerHTML = `
            <tr colspan="5">
                Obtuvimos un error al cargar los productos
            </tr>
        `;
    }
});