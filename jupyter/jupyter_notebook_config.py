##
#c.FileContentsManager.root_dir = ''

## DEPRECATED, use post_save_hook. Will be removed in Notebook 5.0
#c.FileContentsManager.save_script = False

#------------------------------------------------------------------------------
############################################################################################################################## NotebookNotary(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## A class for computing and verifying notebook signatures.

## The hashing algorithm used to sign notebooks.
#c.NotebookNotary.algorithm = 'sha256'

## The sqlite file in which to store notebook signatures. By default, this will
#  be in your Jupyter data directory. You can set it to ':memory:' to disable
#  sqlite writing to the filesystem.
#c.NotebookNotary.db_file = ''

## The secret key with which notebooks are signed.
#c.NotebookNotary.secret = b''

## The file where the secret key is stored.
#c.NotebookNotary.secret_file = ''

## A callable returning the storage backend for notebook signatures. The default
#  uses an SQLite database.
#c.NotebookNotary.store_factory = traitlets.Undefined

#------------------------------------------------------------------------------
# KernelSpecManager(LoggingConfigurable) configuration
#------------------------------------------------------------------------------

## If there is no Python kernelspec registered and the IPython kernel is
#  available, ensure it is added to the spec list.
#c.KernelSpecManager.ensure_native_kernel = True

## The kernel spec class.  This is configurable to allow subclassing of the
#  KernelSpecManager for customized behavior.
#c.KernelSpecManager.kernel_spec_class = 'jupyter_client.kernelspec.KernelSpec'

## Whitelist of allowed kernel names.
#
#  By default, all installed kernels are allowed.
#c.KernelSpecManager.whitelist = set()
c.NotebookApp.ip = '*'
c.NotebookApp.allow_root = True
c.NotebookApp.open_browser = False
#c.NotebookApp.password = u'sha1:0445e8e766f6:fb9718eda28dce472de3c843c3c7d61faaa020c5'
c.NotebookApp.token = ''
c.NotebookManager.notebook_dir = '/notebooks'
