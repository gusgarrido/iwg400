
(function () {
    const container = document.getElementById("alerts-container");
    const alertsUrl = container.dataset.url;

    let last_id = null;
    let checking = false;
    function showAlert(report) {
        const notification = document.createElement("div");
        notification.className = "incident-alert";

        const title = document.createElement("h3");
        title.textContent = "Nuevo incidente: " + report.kind;

        const severity = document.createElement("p");
        severity.textContent = "Severidad: " + report.severity;

        const description = document.createElement("p");
        description.textContent = report.description;

        const close = document.createElement("button");
        close.type = "button";
        close.textContent = "Cerrar";

        close.addEventListener("click", function () {
            notification.remove();
        });
        notification.append(
            title,
            severity,
            description,
            close
        );

        container.prepend(notification);
        setTimeout(function () {
            notification.remove();
        }, 10000);
    }
    async function checkAlerts() {
        if (checking) {
            return;
        }
        checking = true;

        try {
            const params = new URLSearchParams();
            if (last_id !== null) {
                params.set("last_id", last_id);
            }
            const response = await fetch(
                alertsUrl + "?" + params.toString(),
                { cache: "no-store" }
            );
            if (!response.ok) {
                throw new Error("Error al consultar alertas");
            }
            const data = await response.json();
            last_id = data.last_id;

            data.reports.forEach(function (report) {
                showAlert(report);
            });

        } catch (error) {
            console.error("Error de alertas:", error);
        } finally {
            checking = false;
        }
    }
    checkAlerts();
    setInterval(checkAlerts, 5000);
})();
