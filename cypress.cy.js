describe('Verificar el texto de un botón en Detacoop', () => {
    it('Debe verificar que el botón diga "Solicite su Crédito"', () => {
        // Visitar la página
        cy.visit('https://www.detacoop.cl/');

        // Verificar que el texto del elemento sea el esperado
        cy.get('.elementor-button-text')
            .should('be.visible')
            .and('have.text', 'Solicite su Crédito');
    });
});
